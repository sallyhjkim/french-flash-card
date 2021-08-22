<script>
  import { createEventDispatcher } from "svelte";
  import CustomBar from "./CustomBar.svelte";
  const dispatch = createEventDispatcher();

  let customOptions = [
    { side: "french", text: "" },
    { side: "english", text: "" },
  ];

  let saveDisabled = true;
  const handleSave = (e) => {
    dispatch("handleSave", { option: customOptions });
    customOptions = [
      { side: "french", text: "" },
      { side: "english", text: "" },
    ];
    saveDisabled = true;
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
    margin: 20px 0px;
  }
  .saveBtn {
    background: #1976d2;
    outline: none;
    border-radius: 11px;
    width: 85px;
    border: none;
    color: white;
    cursor: pointer;
  }
  .saveBtn:disabled {
    background: #eee;
    color: black;
    cursor: not-allowed;
  }
  .saveBtn:hover:enabled {
    box-shadow: 0 0 0 18px transparent;
    animation: pulse 1s;
  }

  @keyframes pulse {
    from {
      box-shadow: 0 0 0 0#1976d2;
    }
  }
</style>

<div class="custombarInputContainer">
  {#each customOptions as side}
    <div><CustomBar labelName="{side}" on:setLabel="{handleLabel}" /></div>
  {/each}
  <button class="saveBtn" on:click="{handleSave}" disabled="{saveDisabled}"
    >Save</button
  >
</div>
