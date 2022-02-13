<template>
  <main>
    <Navbar />
    <HeroSection />
    <BeakerIcon class="h-5 w-5 text-blue-500" />
    <!-- Mobile Filter -->
    <transition name="fade">
      <div
        v-if="showSelectionBar"
        class="bg-white p-2 px-4 flex flex-row flex-wrap sticky top-30 w-full sticky-filter z-20 border-b-2 border-gray-200 sm:hidden"
      >
        <div
          class="custom-tooltip border-2 bg-gray-100 text-black px-3 py-1 rounded-md absolute text-xs"
          :class="{
            'custom-tooltip-hidden': !showFilterInfo,
          }"
        >
          Hier filtern
        </div>
        <div class="flex flex-wrap mobile-nav-tag-div">
          <template v-for="category in categoryValue">
            <div
              :key="category.id"
              class="border-2 bg-gray-100 border-gray-200 rounded-md flex mr-2 px-1 my-1 text-xs py-1 pr-6 relative"
              :class="category.name"
            >
              {{ category.name }}
              <i
                aria-hidden="true"
                tabindex="1"
                class="custom__remove"
                @click="removeCustomTagItem(category.id)"
              ></i>
            </div>
          </template>
          <template v-for="party in partyValue">
            <div
              :key="party.id"
              class="border-2 bg-gray-100 border-gray-200 rounded-md flex mr-2 px-1 my-1 text-xs py-1"
              :class="party.name"
            >
              {{ party.name }}
            </div>
          </template>
        </div>

        <button
          type="button"
          class="absolute right-4 text-gray-900 bg-gray-100 border border-gray-300 hover:bg-gray-100 focus:ring-2 focus:ring-indigo-300 font-xs rounded-md text-xs px-4 py-2 text-center dark:bg-gray-600 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-700 dark:focus:ring-gray-800"
          @click="handleSecondaryFilter()"
        >
          <AdjustmentsIcon
            size="1.5x"
            class="custom-class"
            :class="{
              'rotate-icon': showSecondaryMobileFilter,
            }"
          />
        </button>
      </div>
    </transition>
    <transition name="fade">
      <div
        v-if="showSecondaryMobileFilter"
        class="bg-white p-2 px-4 flex flex-row flex-wrap sticky top-58 w-full sticky-secondary-filter z-20 border-b-2 border-gray-200"
      >
        <div class="w-full">
          <h2 class="font-bold py-4">Filtern nach Fails</h2>
          <!-- implement text search for mobile here
             <input
            v-model="search"
            type="text"
            placeholder="Textsuche ..."
            class="mobile-search-input text-searchbar mb-4 w-full px-2 transition-all rounded-lg border-2"
          /> -->
          <multiselect
            v-model="categoryValue"
            class="mobile-search-input rounded-lg w-full border-2"
            :options="categories"
            label="name"
            track-by="name"
            :multiple="true"
            :searchable="false"
            placeholder="Kategorie"
            select-label=">"
          >
          </multiselect>
          <multiselect
            v-model="partyValue"
            class="mobile-search-input rounded-lg w-full border-2"
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
            class="mobile-search-input rounded-lg w-full border-2"
            :options="years"
            :multiple="true"
            :searchable="false"
            placeholder="Jahr"
            select-label=">"
          ></multiselect>
        </div>
      </div>
      <!-- <div class="bg-white p-4">
        <input
          v-model="search"
          type="text"
          placeholder="Textsuche ..."
          class="mobile-search-input text-searchbar mb-4 w-full px-2 transition-all rounded-lg border-2"
        />
        <multiselect
          v-model="categoryValue"
          class="mobile-search-input rounded-lg w-full border-2"
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
          class="mobile-search-input rounded-lg w-full border-2"
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
          class="mobile-search-input rounded-lg w-full border-2"
          :options="years"
          :multiple="true"
          :searchable="false"
          placeholder="Jahr"
          select-label=">"
        ></multiselect>
      </div> -->
    </transition>

    <div class="snippet-container pb-8">
      <div class="search-container">
        <div
          class="container sm:flex sm:flex-wrap items-center justify-between max-w-7xl mx-auto py-8 px-4 hidden sm:px-6 lg:px-8"
        >
          <!-- Desktop Filter -->
          <div
            class="grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 md:grid-cols-2 gap-4 w-full hidden md:grid"
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
        class="flex flex-wrap items-center justify-center max-w-7xl mx-auto px-4 pt-6 sm:px-6 lg:px-8"
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
        </div>
      </div>
    </div>
    <Footer />
  </main>
</template>

<script>
import Vue from "vue";
import Multiselect from "vue-multiselect";
import { AdjustmentsIcon } from "@vue-hero-icons/outline";
import SnippetCardSmall from "../components/SnippetCardSmall.vue";

Vue.component("MultiSelect", Multiselect);

export default {
  components: {
    Multiselect,
    SnippetCardSmall,
    AdjustmentsIcon,
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
      showSelectionBar: true,
      showSecondaryMobileFilter: false,
      showFilterInfo: true,
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
  mounted() {
    window.addEventListener("click", this.handleFilterDisplay);
  },
  created() {},
  unmounted() {},
  methods: {
    removeCustomTagItem(item) {
      this.categoryValue.splice(item, 1);
      return null;
    },
    handleFilterDisplay(event) {
      this.showSecondaryMobileFilter === true ||
      this.categoryValue.length > 0 ||
      this.partyValue.length > 0 ||
      this.yearValue.length > 0
        ? (this.showFilterInfo = false)
        : (this.showFilterInfo = true);
    },
    handleSecondaryFilter() {
      this.showSecondaryMobileFilter = !this.showSecondaryMobileFilter;
    },
  },
};
</script>
<!-- New step!
     Add Multiselect CSS. Can be added as a static asset or inside a component. -->
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>
#navbar {
  overflow: hidden;
  background-color: #333;
}

#navbar a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

#navbar a:hover {
  background-color: #ddd;
  color: black;
}

#navbar a.active {
  background-color: #4caf50;
  color: white;
}

.content {
  padding: 16px;
}

.sticky {
  width: 100%;
}

.fade-enter-active {
  transition: all 0.2s;
}
.fade-leave-active {
  transition: all 0.22s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}

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

.multiselect__select::before {
  border-width: 0;
  top: 10px;
  content: url("/down-chevron.svg");
  background-size: cover;
  background-position: center;
  width: 12px;
  height: 12px;
  z-index: 10;
  display: inline-block;
  position: absolute;
}

.multiselect--active {
  border: 2px solid #111;
}

.mobile-search-input {
  border: 0;
  border-radius: 0;
  border-bottom: 1px solid #f4f4f4;
}

.mobile-search-input span,
.mobile-search-input::placeholder {
  font-size: 12px !important;
  color: #222;
}
@media (max-width: 768px) {
  .multiselect__tag {
    border: 1px solid rgb(209, 209, 209);
  }
}

.sticky-filter {
  top: 54px;
  min-height: 54px;
}
.sticky-secondary-filter {
  top: 100px;
  height: 85vh;
}

.custom__remove:after {
  content: "\D7";
  color: #111;
  font-size: 14px;
  cursor: pointer;
  margin-left: 0px;
  position: absolute;
  font-weight: 700;
  font-style: normal;
  text-align: center;
  transition: all 0.2s ease;
  border-radius: 5px;
  right: 0;
  top: 0;
  padding: 4px 6px;
  background: rgba(173, 173, 173, 0.2);
}
.custom__remove:hover:after {
  background: rgb(17, 17, 17);
  border-radius: 5px;
  color: #fff;
}
.mobile-nav-tag-div {
  max-width: 70vw;
}
.custom-class {
  transition: 0.2s ease-in-out;
}
.rotate-icon {
  transform: rotate(90deg);
}
.custom-tooltip {
  opacity: 1;
  right: 100px;
  top: 12px;
  position: absolute;
  transition: 0.2s ease-in-out;
  border: 2px solid #ddd;
}
.custom-tooltip-hidden {
  opacity: 0;
}
.custom-tooltip::after {
  content: "▶";
  position: absolute;
  font-size: 1.1rem;
  right: -14px;
  top: 2px;
  color: #ddd;
}
</style>
