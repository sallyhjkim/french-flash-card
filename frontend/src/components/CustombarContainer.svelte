<script>
  import { createEventDispatcher } from "svelte";
  import CustomBar from "./CustomBar.svelte";
  const dispatch = createEventDispatcher();

  let customOptions = [
    { side: "front", text: "" },
    { side: "back", text: "" },
  ];

  let saveDisabled = true;
  const handleSave = (e) => {
    dispatch("handleSave", { option: customOptions });
    customOptions = [
      { side: "front", text: "" },
      { side: "back", text: "" },
    ];
  };
  const handleLabel = (e) => {
    let tempFlag = false;
    customOptions = customOptions.map((i) => {
      if (i.side === e.detail.side) i.text = e.detail.text;
      if (i.text === "") tempFlag = true;
      return i;
    });
    saveDisabled = tempFlag;
  };
</script>

<style>
  .custombarInputContainer {
    display: flex;
  }
</style>

<div>
  <div class="custombarInputContainer">
    {#each customOptions as side}
      <div><CustomBar labelName="{side}" on:setLabel="{handleLabel}" /></div>
    {/each}
  </div>
  <button on:click="{handleSave}" disabled="{saveDisabled}">Save</button>
</div>
