<template>
    <VCard class="mx-auto mt-5" max-width="500px" color="primary-lighten-5">
        <VCardTitle>Imię Nazwisko</VCardTitle>
        <VCardText>
            <VCard class="mb-2">
                <VCardTitle>Telefony</VCardTitle>
                <VCardText>000-000-000</VCardText>
            </VCard>
            <VCard class="mb-2">
                <VCardTitle>Adresy</VCardTitle>
                <VCardText>000-000-000</VCardText>
            </VCard>
            <VCard class="mb-2">
                <VCardTitle>Umowy</VCardTitle>
                <VCardText>Internet + TV + Telefon</VCardText>
            </VCard>
        </VCardText>
        {{ resp }}
    </VCard>
    
</template>

<script setup>
import { inject, ref} from 'vue'

let resp = ref('');
let $axios = inject('axios')

$axios.get("/api/v1/persons/").then((val) => resp.value = JSON.stringify(val,null,4))


</script>

<style lang="scss">


</style>