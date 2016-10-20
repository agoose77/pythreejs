//
// This file auto-generated with generate-wrappers.js
// Date: Tue Oct 18 2016 14:57:27 GMT-0700 (PDT)
//

var _ = require('underscore');
var widgets = require('jupyter-js-widgets');

var TextureModel = require('./Texture').TextureModel;
var TextureView = require('./Texture').TextureView;


var CubeTextureModel = TextureModel.extend({

    defaults: _.extend({}, TextureModel.prototype.defaults, {

        _view_name: 'CubeTextureView',
        _model_name: 'CubeTextureModel',


    }),

    constructThreeObject: function() {

        return new THREE.CubeTexture();

    },

    createPropertiesArrays: function() {

        TextureModel.prototype.createPropertiesArrays.call(this);

    },

});

var CubeTextureView = TextureView.extend({});

module.exports = {
    CubeTextureView: CubeTextureView,
    CubeTextureModel: CubeTextureModel,
};