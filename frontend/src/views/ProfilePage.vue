<template>
    <VCard class="mx-auto mt-5" max-width="500px" color="primary-lighten-5" v-if="person != null">
        <VCardTitle>{{ person.first_name + ' ' + person.last_name }}</VCardTitle>
        <VCardText>
            <h3>Płeć: {{ person.gender }}</h3>
            <h3>Data urodzenia: {{ person.birth_date }}</h3>
            <h3>PESEL: {{ person.pesel }}</h3>

            <hr style="margin: 30px 0;" color="bg--color-secondary"/>

            <VCard class="mb-2" >
                <VCardTitle>Telefony</VCardTitle>
                <VCardText>
                    <p v-for="telephone in telephones" :key="telephone.id">{{ telephone.telephone }}</p>
                </VCardText>
            </VCard>
            <VCard class="mb-2" >
                <VCardTitle>Adresy</VCardTitle>
                <VCardText>
                    <p v-for="address in addresses" :key="address.id">{{ formatAddress(address) }}</p>
                </VCardText>
            </VCard>
            <VCard class="mb-2">
                <VCardTitle>Umowy</VCardTitle>
                <VCardText>Internet + TV + Telefon</VCardText>
            </VCard>
        </VCardText>
        
    </VCard>
    
</template>

<script setup>
import { inject, ref } from 'vue'

let person = ref(null);
let telephones = ref([]);
let addresses = ref([]);
let $axios = inject('axios')

$axios.get("/api/v1/persons/1/")
      .then((val) => person.value = val.data)
$axios.get("/api/v1/telephones/")
      .then((val) => telephones.value = val.data.results, 
          () => telephones.value = []).then((val) => console.log(val))
$axios.get("/api/v1/addresses/")
      .then((val) => addresses.value = val.data.results, 
          () => addresses.value = []).then((val) => console.log(val))

function formatAddress( { street, house, apartmentNumber }){
    return `${street} ${house}/${apartmentNumber}`
}

</script>

<style lang="scss">


</style>