<template>
  <div
    class="card snippet-card border-2 border-gray-300 p-8 rounded-lg m-4 bg-white"
  >
    <div class="card-body">
      <h5 class="text-xl font-bold border-b-2 border-gray-200 pb-4 mb-4">
        {{ snippet.name }}
      </h5>
      <p class="card-text">
        {{ snippet.description }}
      </p>
      <div class="flex justify-between w-full">
        <p
          class="
        border-2
        py-2
        px-6
        mt-6
        mr-2
        rounded-full
        inline-block
        "
          :class="snippet.category"
        >
          {{ snippet.category }}
        </p>
        <p
          class="
        border-2
        py-2
        px-6
        mt-6
        mr-2
        rounded-full
        inline-block
        "
        >
          Partei
        </p>
      </div>

      <div class="flex flex-col p-4 border-2 border-gray-300 rounded-lg mt-4">
        <template v-for="snippet in snippet.references">
          <a
            :href="snippet"
            target="_blank"
            class="m-2 p-2 border-2 border-white hover:font-bold hover:bg-gray-100 hover:border-gray-200 rounded-md"
            v-bind:key="snippet"
            >{{ snippet }}</a
          >
        </template>
      </div>
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

.tab-content {
  max-height: 0;
  -webkit-transition: max-height 0.35s;
  -o-transition: max-height 0.35s;
  transition: max-height 0.35s;
}
/* :checked - resize to full height */
.tab input:checked ~ .tab-content {
  max-height: 100vh;
}
/* Label formatting when open */
.tab input:checked + label {
  /*@apply text-xl p-5 border-l-2 border-indigo-500 bg-gray-100 text-indigo*/
  font-size: 1.25rem; /*.text-xl*/
  padding: 1.25rem; /*.p-5*/
  border-left-width: 2px; /*.border-l-2*/
  border-color: #6574cd; /*.border-indigo*/
  background-color: #f8fafc; /*.bg-gray-100 */
  color: #6574cd; /*.text-indigo*/
}
/* Icon */
.tab label::after {
  float: right;
  right: 0;
  top: 0;
  display: block;
  width: 1.5em;
  height: 1.5em;
  line-height: 1.5;
  font-size: 1.25rem;
  text-align: center;
  -webkit-transition: all 0.35s;
  -o-transition: all 0.35s;
  transition: all 0.35s;
}
/* Icon formatting - closed */
.tab input[type="checkbox"] + label::after {
  content: "+";
  font-weight: bold; /*.font-bold*/
  border-width: 1px; /*.border*/
  border-radius: 9999px; /*.rounded-full */
  border-color: #b8c2cc; /*.border-grey*/
}
.tab input[type="radio"] + label::after {
  content: "\25BE";
  font-weight: bold; /*.font-bold*/
  border-width: 1px; /*.border*/
  border-radius: 9999px; /*.rounded-full */
  border-color: #b8c2cc; /*.border-grey*/
}
/* Icon formatting - open */
.tab input[type="checkbox"]:checked + label::after {
  transform: rotate(315deg);
  background-color: #6574cd; /*.bg-indigo*/
  color: #f8fafc; /*.text-grey-lightest*/
}
.tab input[type="radio"]:checked + label::after {
  transform: rotateX(180deg);
  background-color: #6574cd; /*.bg-indigo*/
  color: #f8fafc; /*.text-grey-lightest*/
}
</style>
