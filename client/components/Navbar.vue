<template>
  <nav
    class="relative flex flex-wrap items-center justify-between px-2 py-3 bg-gray-900"
  >
    <div
      class="container flex flex-wrap items-center justify-between max-w-4xl mx-auto px-4 sm:px-6 lg:px-8"
    >
      <div
        class="w-full relative flex justify-between lg:w-auto px-4 lg:static lg:block lg:justify-start"
      >
        <a
          class="text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap text-white font-serif"
          href="/"
        >
          politikfails.de
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
          <li class="nav-item">
            <a
              class="px-3 py-2 flex items-center text-xs font-bold leading-snug text-white hover:opacity-75"
              href="/about"
            >
              <i
                class="fab fa-twitter text-lg leading-lg text-white opacity-75"
              /><span class="ml-2">About</span>
            </a>
          </li>
          <li class="nav-item">
            <a
              class="px-3 py-2 flex items-center text-xs font-bold leading-snug text-black hover:opacity-75 bg-green-300 rounded-md"
              href="#pablo"
            >
              <i
                class="fab fa-facebook-square text-lg leading-lg text-white opacity-75"
              /><span class="">Support</span>
            </a>
          </li>
        </ul>
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
