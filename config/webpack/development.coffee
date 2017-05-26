merge = require 'webpack-merge'
baseConfig = require './base.coffee'

module.exports = merge(baseConfig,
  devtool: 'sourcemap'

  stats:
    errorDetails: true

  output:
    pathinfo: true

  module:
    rules: [
      test: require.resolve('jquery')
      use: [{
          loader: 'expose-loader'
          options: 'jQuery'
      },{
          loader: 'expose-loader'
          options: '$'
      }]
    ]
)
