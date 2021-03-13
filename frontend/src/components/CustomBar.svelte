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
  input {
    width: 130px;
    margin-right: 10px;
  }
</style>

<div>
  <span>{labelName.side}</span>
  <input
    id="{labelName.side}"
    type="text"
    on:keyup="{handleInput}"
    value="{labelName.text}"
  />
</div>
