  function clearAll() {
    setGranted(new Set());
  }
// …（中略）…
            <Button variant="outline" data-fn="M00.F04.I04" onClick={clearAll}>
              清空
            </Button>