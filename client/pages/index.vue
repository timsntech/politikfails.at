<template>
  <main>
    <Navbar />
    <h1 class="text-2xl">politikfails.de</h1>
    <p>alle fails auf einen blick</p>
    <template v-for="snippet in snippets">
      <div :key="snippet.id" class="">
        <snippet-card :snippet="snippet">hi</snippet-card>
      </div>
    </template>
  </main>
</template>

<script>
import Navbar from "~/components/Navbar.vue";
import SnippetCard from "~/components/SnippetCard.vue";

export default {
  head() {
    return {
      title: "Recipes list"
    };
  },
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
