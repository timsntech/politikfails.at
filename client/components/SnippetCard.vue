<template>
  <div class="card snippet-card border-2 border-gray-200 p-4 rounded-lg m-4">
    <div class="card-body">
      <h5 class="text-xl font-bold">{{ snippet.name }}</h5>
      <p class="card-text">
        {{ snippet.description }}
      </p>
      <p> {{ snippet.category }} </p>
      <pre> {{ snippet.references }} </pre>
    </div>
  </div>
</template>

<script>
export default {
    props: ["snippet"]
};
</script>

<style>
.card {
  max-width: 900px;
}

</style>
