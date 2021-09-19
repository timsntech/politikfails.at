<template>
  <div
    class="card snippet-card border-2 border-gray-200 p-8 rounded-lg m-4 bg-white"
  >
    <div class="card-body">
      <h5 class="text-xl font-bold border-b-2 border-gray-200 pb-4 mb-4">
        {{ snippet.name }}
      </h5>
      <p class="card-text">
        {{ snippet.description }}
      </p>
      <p
        class="
        border-2
        py-2
        px-6
        mt-6
        rounded-full
        inline-block
        "
        :class="snippet.category"
      >
        {{ snippet.category }}
      </p>
      <!-- <pre> {{ snippet.references }} </pre> -->
    </div>
  </div>
</template>

<script>
export default {
  props: ["snippet"],
  data() {
    return {
      showMenu: false,
      isActive: true,
      hasError: false
    };
  }
};
</script>

<style>
.card {
  max-width: 800px;
  box-shadow: 0px 10px 20px 5px rgba(0, 0, 0, 0.05);
}
.Korruption {
  background: rgb(235, 219, 255);
  border-color: rgb(174, 174, 255);
}
.Verleumdung {
  background: rgb(255, 245, 224);
  border-color: rgb(252, 222, 123);
}
.Betrug {
  background: rgb(213, 255, 219);
  border-color: rgb(156, 253, 156);
}
</style>
