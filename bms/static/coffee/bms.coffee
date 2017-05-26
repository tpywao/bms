jquery = require('jquery')
umi_js = require 'Umi/dist/js/bootstrap'
umi_css = require 'Umi/dist/css/bootstrap'

$(->
  # fix internal ancher link scroll position
  $('a.anchor_link[href^="#"]').click(->
    speed = 400
    href = $(@).attr("href")
    target = if (href == "#" || href == "") then $('html') else $(href)
    headerHeight = $('#navbar-main').height()

    position = target.offset().top - headerHeight
    $('body, html').animate({scrollTop: position}, speed, 'swing')
    return false
  )
)
