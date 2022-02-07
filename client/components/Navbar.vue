<template>
  <nav
    class="sticky top-0 z-50 flex flex-wrap items-center justify-between px-2 bg-white border-b-2 border-gray-200"
  >
    <div
      class="container flex flex-wrap items-center justify-between max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
    >
      <div
        class="relative flex justify-between lg:w-auto sm:px-4 lg:static lg:block lg:justify-start"
      >
        <a
          class="text-md leading-relaxed inline-block mr-4 py-2 pt-2 whitespace-nowrap text-gray-900 font-serif w-28 sm:w-40"
          href="/"
        >
          <img src="/logo.jpg" />
        </a>

        <button
          class="text-white cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
          type="button"
          @click="toggleNavbar()"
        >
          <i class="fas fa-bars"></i>
        </button>
      </div>
      <div
        :class="{ hidden: !showMenu, flex: showMenu }"
        class="lg:flex lg:flex-grow items-center"
      >
        <ul class="flex flex-col lg:flex-row list-none ml-auto">
          <li class="nav-item flex px-4">
            <a
              class="px-3 py-2 flex items-center leading-snug text-sm text-gray-900 hover:opacity-75"
              href="/about"
            >
              <i class="fab fa-twitter text-lg leading-lg opacity-75" /><span
                class="ml-2"
                >About</span
              >
            </a>
          </li>
          <li class="nav-item flex">
            <button
              class="relative inline-flex items-center justify-center p-0.5 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-800"
            >
              <span
                class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0"
              >
                Support Us 🙏
              </span>
            </button>
          </li>
        </ul>
      </div>
      <div class="flex items-center justify-end py-2 sm:p-0">
        <a href="https://github.com/timsntech/politikfails.at" target="_blank">
          <img
            class="mr-2 ml-6 border-2 border-gray-200 p-1 sm:p-2 rounded-full hover:bg-gray-200 transition-all cursor-pointer"
            src="https://img.icons8.com/material-outlined/24/000000/github.png"
          />
        </a>
        <a href="https://twitter.com/politikfails" target="_blank">
          <img
            class="border-2 border-gray-200 p-1 sm:p-2 rounded-full hover:bg-gray-200 transition-all cursor-pointer"
            src="https://img.icons8.com/color/24/000000/twitter--v1.png"
          />
        </a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "PinkNavbar",
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
