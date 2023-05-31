async function weather() {
    let value_cur = await eel.explore_py()();
    document.getElementById("location").value = value_cur['location'];
    document.getElementById("current-temperature").value = value_cur['temp'];
    document.getElementById("wind").value = value_cur['wind'];
    document.getElementById("max-temperature").value = value_cur['maxtemp'];
    document.getElementById("min-temperature").value = value_cur['mintemp'];
}

document.getElementById("btn-sum").onclick = weather;