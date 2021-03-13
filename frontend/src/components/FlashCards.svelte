<script>
  import FlashCard from "./FlashCard.svelte";
  export let flashCards;
</script>

<style></style>

<div>
  {#each flashCards as flashCard}
    <FlashCard flashCard="{flashCard}" />
  {/each}
</div>
