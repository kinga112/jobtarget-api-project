<script setup lang="ts">
  
  import { onMounted, ref } from 'vue'
  import Job from '../components/Job.vue'
  import { type JobType } from '../types/job'

  const jobsData = ref<Array<JobType> | null>(null)

  async function fetchJobs(){
    const response = await fetch('http://127.0.0.1:8000/jobs', {
      method: 'GET',
    });
    if(response.status == 200){
      const data = await response.json()
      jobsData.value = JSON.parse(data)
    }
  }

  onMounted(async () => {
   await fetchJobs()
  });

</script>

<template>
  <div class="flex flex-col gap-5 p-5">
    <div v-for="job in jobsData" :key="job.id">
      <Job :job="job" />
    </div>
  </div>
</template>
