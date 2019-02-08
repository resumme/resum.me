const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    baseUrl: "http://0.0.0.0:8080/",
    outputDir: '../dist/',

    chainWebpack: config => {

        config.optimization
            .splitChunks(false);

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../dashboard/webpack-stats.json'}]);

        config.resolve.alias
            .set('__STATIC__', 'static');

        config.devServer
            .public('http://0.0.0.0:8080')
            .host('0.0.0.0')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["\*"]})
            }
        };