<template>
    <VCard 
        max-width="500px" 
        class="mx-auto"
        color="grey-lighten-5">
        <VCardTitle>Zaloguj się</VCardTitle>
        <VCardText>
            <v-text-field label="Login" v-model="user"></v-text-field>
            <v-text-field 
                label="Hasło"
                v-model="pass"
                :type="showPassword ? 'text' : 'password'"
                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showPassword = !showPassword"></v-text-field>
        </VCardText>
        <VCardActions >
            <VBtn class="ml-auto" @click="zaloguj">Zaloguj</VBtn>
        </VCardActions>
    </VCard>
</template>

<script setup>
import { ref, inject} from 'vue'
import { useAppStore } from '@/store/app';
import { useRouter } from 'vue-router';

let showPassword = ref(false)
let user = ref('')
let pass = ref('')
let $axios = inject('axios')
let appStore = useAppStore();
let router = useRouter();

async function zaloguj() {
    let data = await $axios.post("/api/token/", { username: user.value, password: pass.value } ).then((resp) => resp.data)
    appStore.token.access = data.access;
    appStore.token.refresh = data.refresh;
    router.push({ name: 'Profile' })
}

</script>

<style lang="scss">


</style>