<template>
  <div
    class="card snippet-card border-2 border-gray-300 p-4 rounded-lg bg-white"
  >
    <div class="card-body">
      <div class="">
        <div class="">
          <div class="snippet-image w-full" v-bind:style="{ backgroundImage: 'url(' + snippet.image + ')' }"></div>

<div class="flex justify-between w-full py-2 category-container">
        <div class="flex flex-col items-start">
          <div class="flex flex-row flex-wrap">
            <template v-for="category in snippet.category">
            <div
                class="border-2 font-bold bg-gray-100 border-gray-500 rounded-md flex mr-2 px-2 my-1 text-sm"
                :class="category.name"
                v-bind:key="category"
                >{{ category.name }}
              </div>
            </template>
          </div>
        </div>
        <div class="flex flex-col items-start">
          <div class="flex flex-row flex-wrap flex-row-reverse">
        <template v-for="parties in snippet.parties">
            <p
            v-bind:key="parties"
            class="
              border-2
              px-2
              mr-2
              my-1
              rounded-md
              inline-block text-sm
              "
            :class="parties.name"
              >
          {{ parties.name }}
          </p>
          </template>
          </div>
        </div>
      </div>

          <!-- <p class="text-gray-500 text-xs">Bild: © {{ snippet.image_credits }}</p> -->
        </div>
            <div class="">
                <h5 class="text-md font-bold snippet-card-small-title">
                {{ snippet.name }}
            </h5>
            </div>
      </div>

<div class="flex justify-between items-center">
    <div class="">
        {{ snippet.date }}
    </div>
    <button class="relative inline-flex items-center justify-center p-0.5 mb-2 mr-2 overflow-hidden text-sm font-medium text-gray-900 rounded-md group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-800">
  <span class="relative px-4 py-1 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
      Details  
  </span>
</button>
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
.snippet-image {
    background-position: center;
    background-size: cover;
    border-radius: 0.5rem;
    padding: 4rem 1rem;
}

.snippet-card-small-title {
    min-height: 5rem;
}
@media screen and (min-width: 768px) {
    .category-container {
    min-height:80px;
    }
    .snippet-card-small-title {
    min-height: 6.5rem;
}
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
