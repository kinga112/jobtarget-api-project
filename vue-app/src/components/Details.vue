<script setup lang="ts">

  import { onMounted, ref } from 'vue'
  import type { JobType } from '../types/job'
  import { useRoute } from 'vue-router'
  import Posting from './Posting.vue'

  const error = ref(false)
  const jobData = ref<JobType | null>(null)
  const statusColor = ref('text-green-500')
  const route = useRoute()

  const backButtonStyle = `
    flex justify-center p-2 bg-black 
    text-white font-semibold w-20 h-10 
    float-start rounded-xl`

  async function fetchJobDetails(){
    const response = await fetch(`http://127.0.0.1:8000/job/${route.params.id}`, {
      method: 'GET',
    })

    if(response.status == 200){
      const data = await response.json()
      const json = JSON.parse(data)
      if(json.error){
        error.value = true
      }else{
        jobData.value = json
        if(json.status == 'Inactive'){
          statusColor.value = 'text-red-500'
        }
      }
    }
  }

  onMounted(async () => {
   await fetchJobDetails()
  });

</script>

<template>
  <div class="bg-gray-100 text-black p-5">
    <router-link to="/" :class="backButtonStyle">
      All Jobs
    </router-link>
    <div class="flex flex-col gap-2 p-10">
      <div v-if="error" class="flex flex-col gap-4">
        <div class="text-5xl">Error: Bad id</div>
        <div class="text-lg">The job id is not valid. Please try again later.</div>
      </div>
      <div  v-if="jobData">
        <div class="flex flex-col gap-4">
          <div class="space-x-2 inline-block align-baseline">
            <span class="text-4xl"> {{ jobData!.req_name }}</span>
            <span class=" text-sm"> #{{ jobData!.id }}</span>
          </div>
          <div class="flex gap-1">
            Status:
            <div :class="'font-semibold ' + statusColor">{{ jobData!.status }}</div>
          </div>
          <div> {{ jobData!.location.city }}, {{ jobData!.location.state }}, {{ jobData!.location.country }}</div>
          <div class="text-lg"> {{ jobData!.description }}</div>
          <div class="flex flex-row gap-3">
            <div v-for="posting in jobData.postings" :key="posting.id">
              <Posting :posting="posting" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
