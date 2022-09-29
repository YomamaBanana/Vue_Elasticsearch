<script setup>
import { ref, onMounted } from 'vue'
import NeoVis from 'neovis.js/dist/neovis.js';

// const loading = ref(true);

const neoViz = null;
// const viz = null;

const cypher = ref("");

const config = {
  containerId: "viz",
  neo4j: {
    serverUrl: "****************",
    serverUser: "neo4j",
    serverPassword: "*********************",
  },
  labels: {
    Character: {
      label: "name",
      value: "pagerank",
      group: "community",
      [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
        function: {
          title: (node) => viz.nodeToHtml(node, [
            "name",
            "pagerank"
          ])
        }
      }
    }
  },
  relationships: {
    INTERACTS: {
      value: "weight"
    }
  },
  initialCypher: "MATCH p = (:Character)-[:INTERACTS]->(:Character) RETURN p LIMIT 100;"
};

const query = () => {
  const neoViz = new NeoVis(config);
  neoViz.renderWithCypher(cypher.value);
}

const draw = () => {
  const neoViz = new NeoVis(config);
  neoViz.render();
}

onMounted(() => draw())

defineProps({
  msg: String
})

const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
]

const count = ref(0)
</script>

<template>
  <div>
    <h1>{{ msg }}</h1>

    <div class="card">
      <button type="button" @click="count++">count is {{ count }}</button>
      <p>
        Edit
        <code>components/HelloWorld.vue</code> to test HMR
      </p>
    </div>

    <p>
      Check out
      <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank">create-vue</a>, the official Vue + Vite
      starter
    </p>
    <p>
      Install
      <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
      in your IDE for a better DX
    </p>
    <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
    <!-- <el-table class="table" :data="tableData" style="width: 100%">
      <el-table-column prop="date" label="Date" width="180" />
      <el-table-column prop="name" label="Name" width="180" />
      <el-table-column prop="address" label="Address" />
    </el-table> -->
  </div>
  <h1>Graph below</h1>
  <div id="viz"></div>
  <div>
    Cypher query: <el-input type="textarea" rows="4" cols=50 v-model="cypher"></el-input><br />
  </div>
  <br>
  <div>
    <el-button @click="query">Query</el-button>
    <el-button @click="draw">Draw </el-button>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}

.el-table {
  /* --el-table-border: 10px solid red; */
  --el-table-row-hover-bg-color: red;
  background-color: red !important;
  color: yellow;
  cursor: pointer;
}
</style>
