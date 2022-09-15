<template>
  <h1>Elastic Search Demo</h1>

  <div>
    <h2>キーワード</h2>
    <el-input
      @keyup.enter.native="onSubmit"
      v-model="input"
      placeholder="Please input"
    />
    {{ input }}
  </div>
  <div>
    <h2>出力</h2>
    {{ output.data }}
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const input = ref("");
const output = ref("");

const onSubmit = async () => {
  console.log(`You entered: ${input.value}`);
  input.value = "";

  output.value = await axios.get("http://localhost:8000/");
  console.log(output);
};
</script>
