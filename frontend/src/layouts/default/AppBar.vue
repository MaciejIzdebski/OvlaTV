<template>
  <v-app-bar flat>
    <v-app-bar-title>
      

      <span style="margin-top: 1em;"><v-icon :icon="icon" />vlaTV</span>
    </v-app-bar-title>
  </v-app-bar>
</template>

<script setup>
import { ref } from 'vue'
let icon = ref('mdi-circle-slice-6')
</script>
