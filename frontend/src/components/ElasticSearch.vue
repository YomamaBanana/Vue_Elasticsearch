<template>
  <h1>Elastic Search Demo</h1>

  <div>
    <h3>キーワード</h3>
    <el-input
      @keyup.enter.native="onSubmit"
      v-model="input"
      placeholder="Please input"
    />
  </div>
  {{ input }}
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const input = ref("");

const onSubmit = async () => {
  console.log(`You entered: ${input.value}`);
  input.value = "";

  const res = await axios.get("http://localhost:8000/");
  console.log(res.data.message);
};
</script>
