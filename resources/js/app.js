import Alpine from 'alpinejs'
import collapse from '@alpinejs/collapse'

require("./bootstrap.js")

window.Alpine = Alpine

Alpine.plugin(collapse)

Alpine.magic('clipboard', () => {
  return subject => navigator.clipboard.writeText(subject)
})

// For navbar interactivity
Alpine.data('menu', () => ({
  opened: false,
  active: null,
  init () {
  },
  toggle () {
    this.opened = !this.opened
  },
  isActive() {
    return window.location.pathname == this.$el.pathname
  }
}))

// For FAQ accordion
Alpine.data('accordion', (initQuestions=[]) => ({
  currentId: null,
  questions: [],
  init () {
    this.questions = initQuestions
  },
  toggle (id) {
    if (this.currentId == id) {
      this.currentId = null
    } else {
      this.currentId = id
    }
  }
}))

Alpine.start()
