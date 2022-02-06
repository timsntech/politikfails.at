module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    "plugin:vue/vue3-essential",
    "plugin:vue/vue3-recommended",
    "@nuxtjs",
    "plugin:prettier/recommended",
    "prettier",
  ],
  parserOptions: {
    ecmaVersion: 12,
    parser: "@babel/eslint-parser",
    sourceType: "module",
    requireConfigFile: false,
  },
  plugins: ["vue"],
  rules: {
    "vue/multi-word-component-names": "warn",
    "vue/no-v-for-template-key-on-child": "off",
    "no-unused-vars": "warn",
    "space-in-parens": "off",
    "computed-property-spacing": "off",
  },
};
