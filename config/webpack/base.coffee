{ basename, dirname, join, relative, resolve } = require 'path'
{ env } = require 'process'
{ readFileSync } = require 'fs'
{ safeLoad } = require 'js-yaml'
{ sync } = require 'glob'
webpack = require 'webpack'
extname = require('path-complete-extname')
ExtractTextPlugin = require 'extract-text-webpack-plugin'

configPath = resolve('config', 'webpack')
paths = safeLoad(readFileSync(join(configPath, 'paths.yml'), 'utf8'))[env.NODE_ENV]
loadersDir = join(__dirname, 'loaders')

extensionGlob = "**/*{#{paths.extensions.join(',')}}*"
packPaths = sync(join(paths.source, paths.entry, extensionGlob))

module.exports =
  entry:
    packPaths.reduce(
      (map, entry) ->
        local_map = map
        namespace = relative(join(paths.source, paths.entry), dirname(entry))
        local_map[join(namespace, basename(entry, extname(entry)))] = resolve(entry)
        return local_map
      {})

  output:
    filename: 'js/bundle.js'
    path: resolve(paths.output)

  module:
    rules:
      sync(join(loadersDir, '*.coffee'))
        .map((loader) -> require loader)

  resolve:
    extensions: paths.extensions
    modules: [
      resolve(paths.source)
      resolve(paths.node_modules)
      resolve(paths.bower_components)
    ]

  plugins: [
    new ExtractTextPlugin(filename: 'css/bundle.css')
    new webpack.ProvidePlugin(
      $: 'jquery'
      jQuery: 'jquery'
      )
  ]
