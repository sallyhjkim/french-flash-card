<script>
  export let flashCard;
  let side = "french";

  const flipCard = (e) => {
    side = side === "french" ? "english" : "french";
  };
</script>

<style>
  .flashCardBox {
    display: inline-block;
    margin: 0 auto;
    padding: 0 12px;
    perspective: 900px;
    text-align: center;
    cursor: pointer;
  }

  .flashCardInner {
    position: relative;
    width: 300px;
    height: 150px;
    transition: all 0.7s ease;
    transform-style: preserve-3d;
  }

  .card {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    position: absolute;
    background: #f7f7f7;
    left: 0;
    width: 300px;
    height: 150px;
    border-radius: 5px;
    box-shadow: 0 27px 55px 0 rgba(0, 0, 0, 0.3),
      0 17px 17px 0 rgba(0, 0, 0, 0.15);
    backface-visibility: hidden;
  }

  .frontTransform0 {
    transform: rotateX(0deg);
  }

  .frontTransform180 {
    transform: rotateX(180deg);
  }

  .backTransform {
    transform: rotateX(180deg);
  }
</style>

<div class="flashCardBox" on:click="{flipCard}">
  <div
    class="flashCardInner {side === 'french'
      ? 'frontTransform0'
      : 'frontTransform180'}"
  >
    <div class="flashCardItem card">{flashCard.french}</div>
    <div class="flashCardItem card backTransform">{flashCard.english}</div>
  </div>
</div>
