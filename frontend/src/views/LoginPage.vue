<template>
    <VCard 
        max-width="500px" 
        class="mx-auto"
        color="grey-lighten-5">
        <VCardTitle>Zaloguj się</VCardTitle>
        <VCardText>
            <v-text-field label="Login"></v-text-field>
            <v-text-field 
                label="Hasło" 
                :type="showPassword ? 'text' : 'password'"
                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showPassword = !showPassword"></v-text-field>
        </VCardText>
        <VCardActions >
            <VBtn class="ml-auto">Zaloguj</VBtn>
        </VCardActions>
    </VCard>
</template>

<script setup>
import { ref } from 'vue'
let showPassword = ref(false)
</script>

<style lang="scss">


</style>