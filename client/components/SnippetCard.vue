<template>
  <div
    class="card snippet-card border-2 border-gray-300 p-8 rounded-lg m-4 bg-white"
  >
    <div class="card-body">
      <div class="grid grid-cols-3 gap-4">
        <div class="">
          <img :src=snippet.image class="rounded-md m-0">
          <p class="text-gray-500">© {{ snippet.image_credits }}</p>
        </div>
      <div class="col-span-2">
        <h5 class="text-3xl font-bold border-b-2 border-gray-200 pb-4 mb-4">
        {{ snippet.name }}
      </h5>
      </div>
      </div>
      

      <div class="flex justify-between w-full">
        <div class="flex flex-col justify-center items-start">
          <strong class="pb-2 pt-2">Tags:</strong>
          <div class="flex flex-row">
            <template v-for="category in snippet.category">
            <div
                class="p-2 border-2 border-white font-bold bg-gray-100 border-gray-700 rounded-md flex justify-center items-center mr-2"
                :class="category.name"
                v-bind:key="category"
                >{{ category.name }}
              </div>
            </template>
          </div>
        </div>
        <div class="flex flex-col justify-center items-start">
          <strong class="pb-2">Involvierte Parteien:</strong>
          <div class="flex flex-row">
        <template v-for="parties in snippet.parties">
            <p
            v-bind:key="parties"
            class="
              border-2
              py-2
              px-6
              mr-2
              rounded-md
              inline-block
              "
            :class="parties.name"
              >
          {{ parties.name }}
          </p>
          </template>
          </div>
        </div>
        
      </div>

      <p class="card-text mb-4 pt-6">
        {{ snippet.description }}
      </p>

      <div class="flex flex-col p-4 border-2 border-gray-300 rounded-lg mt-4">
        <strong>Referenzen & Quellen</strong>
        <template v-for="snippet in snippet.sources">
          <a
            :href="snippet"
            target="_blank"
            class="p-2 border-2 border-white hover:font-bold hover:bg-gray-100 hover:border-gray-200 rounded-md"
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


.ÖVP {
  background: #63C3D0;
  border-color: #549da7;
}
.Bündnis90 {
  background: #a7eec3;  
  border-color: #70b48c;
}
.SPÖ {
  background: #f1c3bd;  
  border-color: #b96b6b;
}
.FPÖ {
  background: #a5b4f5;  
  border-color: #3f5ab3;
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
