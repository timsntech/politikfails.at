<template>
  <footer
    class="relative flex flex-wrap items-center justify-between px-2 bg-white border-b-2 border-gray-200"
  >
    <div
      class="container flex flex-wrap items-center justify-between max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
    >
      <div
        class="h-54 py-4 md:h-20 grid grid-cols-1 sm:grid-cols-1 lg:grid-cols-3 md:grid-cols-3 gap-3 content-center w-full"
      >
        <div
          class="w-28 md:w-40 flex justify-center item-center md:justify-start"
        >
          <a href="/">
            <img src="/logo.jpg" />
          </a>
        </div>
        <div class="flex items-center justify-start md:justify-center">
          <p class="text-sm text-gray-500">
            Built with 🖤 in Nuxt.js + Django.
          </p>
        </div>
        <div class="flex items-center justify-start md:justify-end">
          <a
            href="https://github.com/timsntech/politikfails.at"
            target="_blank"
          >
            <img
              class="mr-2 border-2 border-gray-200 p-2 rounded-full hover:bg-gray-200 transition-all cursor-pointer"
              src="https://img.icons8.com/material-outlined/24/000000/github.png"
            />
          </a>
          <a href="https://twitter.com/politikfails" target="_blank">
            <img
              class="border-2 border-gray-200 p-2 rounded-full hover:bg-gray-200 transition-all cursor-pointer"
              src="https://img.icons8.com/color/24/000000/twitter--v1.png"
            />
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      showMenu: false,
    };
  },
  methods: {
    toggleNavbar() {
      this.showMenu = !this.showMenu;
    },
  },
};
</script>
