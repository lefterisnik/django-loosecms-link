var jQuery = django.jQuery || {};

(function($){
    'use strict';

    $(document).ready(function() {
        var bestTitles = new Bloodhound({
            datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
            queryTokenizer: Bloodhound.tokenizers.whitespace,
            prefetch: '/admin/loosecms_link/link/api/get_title/',
            remote: {
                url: '/admin/loosecms_link/link/api/get_title/?title=%QUERY',
                wildcard: '%QUERY'
            }
        });

        var bestUrls = new Bloodhound({
            datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
            queryTokenizer: Bloodhound.tokenizers.whitespace,
            prefetch: '/admin/loosecms_link/link/api/get_url/',
            remote: {
                url: '/admin/loosecms_link/link/api/get_url/?url=%QUERY',
                wildcard: '%QUERY'
            }
        });

        $('#id_title').typeahead(null, {
            name: 'link-title',
            display: 'title',
            source: bestTitles
        });

        $('#id_url').typeahead(null, {
            name: 'link-url',
            display: 'url',
            source: bestUrls
        });

        $('.tt-query').css('background-color','#fff');

    });

}) (django.jQuery)