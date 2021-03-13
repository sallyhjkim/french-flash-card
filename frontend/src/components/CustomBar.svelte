<script>
  export let labelName;
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  const handleInput = (e) => {
    const side = e.target.id;
    const val = e.target.value;
    dispatch("setLabel", { side: side, text: val });
  };
</script>

<style>
  .customInputBar {
    margin: 0px 10px;
    position: relative;
  }
  .customInput {
    padding: 8px;
    display: block;
    border: none;
    border-bottom: 1px solid #000;
    width: 100%;
    background: transparent;
  }
  .customInputLabel {
    position: absolute;
    top: -20px;
    left: 5px;
  }
</style>

<div class="customInputBar">
  <input
    class="customInput"
    id="{labelName.side}"
    type="text"
    on:keyup="{handleInput}"
    value="{labelName.text}"
  />
  <span class="customInputLabel">{labelName.side}</span>
</div>
