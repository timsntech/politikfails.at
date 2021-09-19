<template>
  <main>
    <Navbar />
    <HeroSection />
    <div class="snippet-container">
      <div
        class="flex flex-wrap items-center justify-center max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
      >
        <div class="-mt-12">
          <template v-for="snippet in snippets">
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
import SnippetCard from "~/components/SnippetCard.vue";

export default {
  components: {
    SnippetCard
  },
  async asyncData({ $axios, params }) {
    try {
      let snippets = await $axios.$get(`/snippets/`);

      return { snippets };
    } catch (e) {
      console.log("hi");
      return { snippets: [] };
    }
  },
  data() {
    return {
      snippets: []
    };
  }
};
</script>

<style>
.snippet-container {
  background-color: #f6f6f6;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' viewBox='0 0 4 4'%3E%3Cpath fill='%23b0b0b0' fill-opacity='0.4' d='M1 3h1v1H1V3zm2-2h1v1H3V1z'%3E%3C/path%3E%3C/svg%3E");
}
</style>
