<template>
  <main>
    <Navbar />
    <HeroSection />
    <div class="search-container ">
      <div
        class="container flex flex-wrap items-center justify-between max-w-4xl mx-auto pt-8 pb-14 px-14"
      >
        <input
          type="text"
          v-model="search"
          placeholder="Textsuche ..."
          class="searchbar text-searchbar mb-4 py-2 h-full w-full px-2 transition-all rounded-lg border-2"
        />

        <div class="grid grid-cols-3 gap-4 w-full">
          <multiselect
            class="searchbar rounded-lg w-full border-2"
            v-model="categoryValue"
            :options="categories"
            label="name" 
            track-by="name"
            :multiple="true"
            :searchable="false"
            placeholder="Kategorie"
            select-label=">"
          ></multiselect>
          <multiselect
            class="searchbar  rounded-lg w-full border-2"
            v-model="partyValue"
            :options="parties"
            :multiple="true"
            :searchable="false"
            label="name" 
            track-by="name"
            placeholder="Partei"
            select-label=">"
          ></multiselect>
          <multiselect
            class="searchbar  rounded-lg w-full border-2"
            v-model="yearValue"
            :options="years"
            :multiple="true"
            :searchable="false"
            placeholder="Jahr"
            select-label=">"
          ></multiselect>
        </div>
      </div>
    </div>

    <div class="snippet-container border-t-2 border-gray-300">
      <div
        class="flex flex-wrap items-center justify-center max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
      >
        <div class="-mt-24">
          <div class="p-6"></div>
          <template v-for="snippet in !filteredList ? snippets : filteredList">
            <div :key="snippet.id" class="">
              <snippet-card :snippet="snippet" />
            </div>
          </template>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import Vue from "vue";
import SnippetCard from "~/components/SnippetCard.vue";
import Multiselect from "vue-multiselect";
Vue.component("multiselect", Multiselect);

export default {
  components: {
    SnippetCard,
    Multiselect
  },
  async asyncData({ $axios, params }) {
    try {
      // get snippets (fails)
      let snippets = await $axios.$get(`/snippets/`);

      // get categories
      let categories = await $axios.$get(`/categories/`);

      // get political parties
      let parties = await $axios.$get(`/parties/`);

      // return data
      return { snippets, categories, parties };
    } catch (e) {
      console.log(e)
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
  methods: {},
  computed: {
    filteredList() {

      // filter all snippets
      return this.snippets.filter(snippet => {

        // no filter selected, except text search
        if (this.partyValue.length === 0 && this.categoryValue.length === 0 && this.yearValue.length === 0) {
          return snippet.name.toLowerCase().includes(this.search.toLowerCase())
        }

        // party filter selected + and text search
        if (this.partyValue.length !== 0 && this.categoryValue.length === 0 && this.yearValue.length === 0) {
        return snippet.name.toLowerCase().includes(this.search.toLowerCase()) && 
               snippet.parties.filter((o1) => this.partyValue.some((o2) => o1.id === o2.id)).length !== 0
        }

        // category filter selected + text search
        if (this.categoryValue.length !== 0 && this.partyValue.length === 0 && this.yearValue.length === 0) {
        return snippet.name.toLowerCase().includes(this.search.toLowerCase()) && 
               snippet.category.filter((o1) => this.categoryValue.some((o2) => o1.id === o2.id)).length !== 0
        }

        // year filter selected + text search
        if (this.yearValue.length !== 0 && this.categoryValue.length === 0 && this.partyValue.length === 0) {
        return snippet.name.toLowerCase().includes(this.search.toLowerCase()) && 
               snippet.date.includes(this.yearValue)
        }

        // category and party filter selected + text search
        if (this.categoryValue.length !== 0 && this.partyValue.length !== 0 && this.yearValue.length === 0) {
        return snippet.name.toLowerCase().includes(this.search.toLowerCase()) && 
               snippet.category.filter((o1) => this.categoryValue.some((o2) => o1.id === o2.id)).length !== 0 &&
               snippet.parties.filter((o1) => this.partyValue.some((o2) => o1.id === o2.id)).length !== 0
        }

        // category and year filter selected + text search
        if (this.categoryValue.length !== 0 && this.partyValue.length === 0 && this.yearValue.length !== 0) {
        return snippet.name.toLowerCase().includes(this.search.toLowerCase()) && 
               snippet.category.filter((o1) => this.categoryValue.some((o2) => o1.id === o2.id)).length !== 0 &&
               snippet.date.includes(this.yearValue)
        }

        // party and year filter selected + text search
        if (this.categoryValue.length === 0 && this.partyValue.length !== 0 && this.yearValue.length !== 0) {
        return snippet.name.toLowerCase().includes(this.search.toLowerCase()) && 
               snippet.parties.filter((o1) => this.partyValue.some((o2) => o1.id === o2.id)).length !== 0 &&
               snippet.date.includes(this.yearValue)
        }

        // category, party and year filter selected + text search
        if (this.categoryValue.length !== 0 && this.partyValue.length !== 0 && this.yearValue.length !== 0) {
        return snippet.name.toLowerCase().includes(this.search.toLowerCase()) &&
               snippet.category.filter((o1) => this.categoryValue.some((o2) => o1.id === o2.id)).length !== 0 && 
               snippet.parties.filter((o1) => this.partyValue.some((o2) => o1.id === o2.id)).length !== 0 &&
               snippet.date.includes(this.yearValue)
        }

      })
    }
    
  }
};
</script>
<!-- New step!
     Add Multiselect CSS. Can be added as a static asset or inside a component. -->
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>
.snippet-container {
  background-color: #f6f6f6;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' viewBox='0 0 4 4'%3E%3Cpath fill='%23b0b0b0' fill-opacity='0.4' d='M1 3h1v1H1V3zm2-2h1v1H3V1z'%3E%3C/path%3E%3C/svg%3E");
}

.search-container {
  background-color: #ffffff;
}

.text-searchbar {
  padding: 14px 10px;
}

.multiselect__tag {
  background: #f1f1f1;
  border: 2px solid #111;
  color: #111;
}
.multiselect__tag-icon:focus, .multiselect__tag-icon:hover {
  background: #111;
  border-radius: 0px;
}
.multiselect__option--highlight {
  background: #ddd;
  color: #111;
}
.multiselect__tags {
  padding: 11px 40px 0 8px;
  border: 0px;
}

</style>
