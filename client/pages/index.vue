<template>
  <main>
    <Navbar />
    <HeroSection />

    <div class="snippet-container pb-8">
      <div class="search-container">
        <div
          class="container flex flex-wrap items-center justify-between max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8"
        >
          <div
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 md:grid-cols-2 gap-4 w-full"
          >
            <input
              v-model="search"
              type="text"
              placeholder="Textsuche ..."
              class="searchbar text-searchbar mb-4 w-full px-2 transition-all rounded-lg border-2"
            />
            <multiselect
              v-model="categoryValue"
              class="searchbar rounded-lg w-full border-2"
              :options="categories"
              label="name"
              track-by="name"
              :multiple="true"
              :searchable="false"
              placeholder="Kategorie"
              select-label=">"
            ></multiselect>
            <multiselect
              v-model="partyValue"
              class="searchbar rounded-lg w-full border-2"
              :options="parties"
              :multiple="true"
              :searchable="false"
              label="name"
              track-by="name"
              placeholder="Partei"
              select-label=">"
            ></multiselect>
            <multiselect
              v-model="yearValue"
              class="searchbar rounded-lg w-full border-2"
              :options="years"
              :multiple="true"
              :searchable="false"
              placeholder="Jahr"
              select-label=">"
            ></multiselect>
          </div>
        </div>
      </div>

      <div
        class="flex flex-wrap items-center justify-center max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
      >
        <div class="">
          <div
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 md:grid-cols-3 max-w-7xl gap-2"
          >
            <template
              v-for="snippet in !filteredList ? snippets : filteredList"
            >
              <SnippetCardSmall :key="snippet.id" :snippet="snippet" />
            </template>
          </div>
          <div v-if="filteredList.length === 0">
            <div class="p-2">
              <div
                class="flex-col sm:flex-row inline-flex items-center bg-white leading-none text-purple-600 rounded-md p-8 py-8 my-12 shadow text-teal text-sm"
              >
                <span
                  class="inline-flex bg-indigo-600 text-white rounded-full h-6 px-3 mb-4 sm:m-2 justify-center items-center"
                  >No Content</span
                >
                <span class="inline-flex px-2 text-gray-900"
                  >Für die gewählte Auswahl ist (noch) nichts verfügbar 😉
                </span>
              </div>
            </div>
          </div>

          <!-- <template v-for="snippet in !filteredList ? snippets : filteredList">
            <div :key="snippet.id" class="">
              <snippet-card :snippet="snippet" />
            </div>
          </template> -->
        </div>
      </div>
    </div>
    <Footer />
  </main>
</template>

<script>
import Vue from "vue";
import Multiselect from "vue-multiselect";
import SnippetCardSmall from "../components/SnippetCardSmall.vue";
Vue.component("MultiSelect", Multiselect);

export default {
  components: {
    Multiselect,
    SnippetCardSmall,
  },
  async asyncData({ $axios }) {
    try {
      // get snippets (fails)
      const snippets = await $axios.$get("/snippets/");

      // get categories
      const categories = await $axios.$get("/categories/");

      // get political parties
      const parties = await $axios.$get("/parties/");

      // return data
      return { snippets, categories, parties };
    } catch (e) {
      return { snippets: [], categories: [], parties: [] };
    }
  },
  data() {
    return {
      snippets: [],
      categories: [],
      parties: [],
      years: ["2020", "2021", "2022"],
      search: "",
      categoryValue: [],
      partyValue: [],
      yearValue: [],
    };
  },
  computed: {
    filteredList() {
      // filter all snippets
      return this.snippets.filter((snippet) => {
        // no filter selected, except text search
        if (
          this.partyValue.length === 0 &&
          this.categoryValue.length === 0 &&
          this.yearValue.length === 0
        ) {
          return snippet.name.toLowerCase().includes(this.search.toLowerCase());
        }

        // party filter selected + and text search
        if (
          this.partyValue.length !== 0 &&
          this.categoryValue.length === 0 &&
          this.yearValue.length === 0
        ) {
          return (
            snippet.name.toLowerCase().includes(this.search.toLowerCase()) &&
            snippet.parties.filter((o1) =>
              this.partyValue.some((o2) => o1.id === o2.id)
            ).length !== 0
          );
        }

        // category filter selected + text search
        if (
          this.categoryValue.length !== 0 &&
          this.partyValue.length === 0 &&
          this.yearValue.length === 0
        ) {
          return (
            snippet.name.toLowerCase().includes(this.search.toLowerCase()) &&
            snippet.category.filter((o1) =>
              this.categoryValue.some((o2) => o1.id === o2.id)
            ).length !== 0
          );
        }

        // year filter selected + text search
        if (
          this.yearValue.length !== 0 &&
          this.categoryValue.length === 0 &&
          this.partyValue.length === 0
        ) {
          return (
            snippet.name.toLowerCase().includes(this.search.toLowerCase()) &&
            snippet.date.includes(this.yearValue)
          );
        }

        // category and party filter selected + text search
        if (
          this.categoryValue.length !== 0 &&
          this.partyValue.length !== 0 &&
          this.yearValue.length === 0
        ) {
          return (
            snippet.name.toLowerCase().includes(this.search.toLowerCase()) &&
            snippet.category.filter((o1) =>
              this.categoryValue.some((o2) => o1.id === o2.id)
            ).length !== 0 &&
            snippet.parties.filter((o1) =>
              this.partyValue.some((o2) => o1.id === o2.id)
            ).length !== 0
          );
        }

        // category and year filter selected + text search
        if (
          this.categoryValue.length !== 0 &&
          this.partyValue.length === 0 &&
          this.yearValue.length !== 0
        ) {
          return (
            snippet.name.toLowerCase().includes(this.search.toLowerCase()) &&
            snippet.category.filter((o1) =>
              this.categoryValue.some((o2) => o1.id === o2.id)
            ).length !== 0 &&
            snippet.date.includes(this.yearValue)
          );
        }

        // party and year filter selected + text search
        if (
          this.categoryValue.length === 0 &&
          this.partyValue.length !== 0 &&
          this.yearValue.length !== 0
        ) {
          return (
            snippet.name.toLowerCase().includes(this.search.toLowerCase()) &&
            snippet.parties.filter((o1) =>
              this.partyValue.some((o2) => o1.id === o2.id)
            ).length !== 0 &&
            snippet.date.includes(this.yearValue)
          );
        }

        // category, party and year filter selected + text search
        if (
          this.categoryValue.length !== 0 &&
          this.partyValue.length !== 0 &&
          this.yearValue.length !== 0
        ) {
          return (
            snippet.name.toLowerCase().includes(this.search.toLowerCase()) &&
            snippet.category.filter((o1) =>
              this.categoryValue.some((o2) => o1.id === o2.id)
            ).length !== 0 &&
            snippet.parties.filter((o1) =>
              this.partyValue.some((o2) => o1.id === o2.id)
            ).length !== 0 &&
            snippet.date.includes(this.yearValue)
          );
        }
        return false;
      });
    },
  },
  methods: {},
};
</script>
<!-- New step!
     Add Multiselect CSS. Can be added as a static asset or inside a component. -->
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>
#__nuxt {
  font-family: "Open Sans", sans-serif;
}
.snippet-container {
  background-color: #f6f6f6;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' viewBox='0 0 4 4'%3E%3Cpath fill='%23b0b0b0' fill-opacity='0.4' d='M1 3h1v1H1V3zm2-2h1v1H3V1z'%3E%3C/path%3E%3C/svg%3E");
}

.searchbar {
  border: 2px solid #ddd;
  background-color: #fff;
}

.text-searchbar {
  padding: 14px 10px;
  margin: 0;
}

.multiselect__tag {
  background: #f1f1f1;
  border: 2px solid #111;
  color: #111;
}
.multiselect__tag-icon:focus,
.multiselect__tag-icon:hover {
  background: #111;
  border-radius: 0px;
}
.multiselect__option--highlight {
  background: #ddd;
  color: #111;
}
.multiselect__tags {
  padding: 4px 10px;
  border: 0px;
  padding-top: 10px;
}
.multiselect__placeholder {
  padding-top: 10px;
}
.multiselect__select {
  top: 6px;
}
.multiselect--active {
  border: 2px solid #111;
}
</style>
