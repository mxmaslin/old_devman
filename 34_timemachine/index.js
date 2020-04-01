var TIMEOUT_IN_SECS = 3 * 60
var NOTIFICATION_INTERVAL = 30
var TEMPLATE = '<h1 style="color:#666"><span class="js-timer-minutes">00</span>:<span class="js-timer-seconds">00</span></h1>'

function padZero(number){
  return ("00" + String(number)).slice(-2);
}

class Timer{
  // IE does not support new style classes yet
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes
  constructor(timeout_in_secs){
    this.initial_timeout_in_secs = timeout_in_secs
    this.reset()
  }
  getTimestampInSecs(){
    var timestampInMilliseconds = new Date().getTime()
    return Math.round(timestampInMilliseconds/1000)
  }
  start(){
    if (this.isRunning)
      return
    this.timestampOnStart = this.getTimestampInSecs()
    this.isRunning = true
  }
  stop(){
    if (!this.isRunning)
      return
    this.timeout_in_secs = this.calculateSecsLeft()
    this.timestampOnStart = null
    this.isRunning = false
  }
  reset(timeout_in_secs){
    this.isRunning = false
    this.timestampOnStart = null
    this.timeout_in_secs = this.initial_timeout_in_secs
  }
  calculateSecsLeft(){
    if (!this.isRunning)
      return this.timeout_in_secs
    var currentTimestamp = this.getTimestampInSecs()
    var secsGone = currentTimestamp - this.timestampOnStart
    return Math.max(this.timeout_in_secs - secsGone, 0)
  }
}

class TimerWidget{
  // IE does not support new style classes yet
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes
  construct(){
    this.timerContainer = this.minutes_element = this.seconds_element = null
  }
  mount(rootTag){
    if (this.timerContainer)
      this.unmount()

    // adds HTML tag to current page
    this.timerContainer = document.createElement('div')

    this.timerContainer.setAttribute("style", "height:100px;position:fixed;padding:20px;background: #fff;opacity:0.5;z-index:10")

    this.timerContainer.innerHTML = TEMPLATE

    rootTag.insertBefore(this.timerContainer, rootTag.firstChild)

    this.minutes_element = this.timerContainer.getElementsByClassName('js-timer-minutes')[0]
    this.seconds_element = this.timerContainer.getElementsByClassName('js-timer-seconds')[0]
  }
  update(secsLeft){
    var minutes = Math.floor(secsLeft / 60);
    var seconds = secsLeft - minutes * 60;

    this.minutes_element.innerHTML = padZero(minutes)
    this.seconds_element.innerHTML = padZero(seconds)
  }
  unmount(){
    if (!this.timerContainer)
      return
    this.timerContainer.remove()
    this.timerContainer = this.minutes_element = this.seconds_element = null
  }
}


function main(){

  var timer = new Timer(TIMEOUT_IN_SECS)
  var alertTimer = new Timer(NOTIFICATION_INTERVAL)
  var timerWiget = new TimerWidget()
  var intervalId = null
  var alertIntervalId = null

  timerWiget.mount(document.body)

  function handleIntervalTick(){
    var secsLeft = timer.calculateSecsLeft()
    timerWiget.update(secsLeft)
  }

  var quotes = ['Прокрастинация - первый шаг к теплотрассе', 'Хватит тупить, код сам себя не напишет', 'Хабр хорошо, а PyCharm лучше']

  var wasShown = false

  function handleAlertDisplay(){
    var randomIdx = Math.floor(Math.random() * quotes.length)
    if (timer.calculateSecsLeft() === 0){
      if (!wasShown) {
        alert(quotes[randomIdx])
        wasShown = true
        alertTimer.reset()
        alertTimer.start()
      }
      if (alertTimer.calculateSecsLeft() === 0){
        alert(quotes[randomIdx])
        alertTimer.reset()
        alertTimer.start()
      }
    }
  }

  function handleVisibilityChange(){
    if (document.hidden) {
      timer.stop()
      clearInterval(intervalId)
      clearInterval(alertIntervalId)
      intervalId = null
      alertIntervalId = null
      alertTimer.reset()
      alertTimer.stop()
    } else {
      timer.start()
      alertTimer.start()
      intervalId = intervalId || setInterval(handleIntervalTick, 300)
      alertIntervalId = alertIntervalId || setInterval(handleAlertDisplay, 300)
    }
  }

  // https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API
  document.addEventListener("visibilitychange", handleVisibilityChange, false);
  handleVisibilityChange()
}

if (document.readyState === "complete" || document.readyState === "loaded") {
  main();
} else {
  // initialize timer when page ready for presentation
  window.addEventListener('DOMContentLoaded', main);
}


