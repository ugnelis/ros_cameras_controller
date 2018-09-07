import angular from 'angular';

function mjpeg() {
    return {
        restrict: 'E',
        replace: true,
        template: '<span></span>',
        scope: {
            'url': '@',
            'width': '@?'
        },
        link: function (scope, element, attrs) {
            scope.width = angular.isDefined(scope.width) ? scope.width : '100%';

            scope.$watch('url', function (newVal, oldVal) {
                if (newVal) {
                    let iframe = document.createElement('iframe');
                    iframe.setAttribute('width', scope.width);
                    iframe.setAttribute('frameborder', '0');
                    iframe.setAttribute('scrolling', 'no');
                    element.replaceWith(iframe);

                    let iframeHtml = '<html><head><base target="_parent" /><style type="text/css">html, body { margin: 0; padding: 0; height: 100%; width: 100%; }</style><script> function resizeParent() { let iframes = window.top.document.getElementsByTagName("iframe"); for (let i = 0, length = iframes.length; i < length; i++) { let iframe = iframes[i]; let iframeDocument = iframe.contentDocument || iframe.contentWindow.document; if (iframeDocument === document) { iframe.height = document.body.scrollHeight; } } }</script></head><body onresize="resizeParent()"><img src="' + newVal + '" style="width: 100%; height: auto" onload="resizeParent()" /></body></html>';

                    let iframeDocument = iframe.document;
                    if (iframe.contentDocument) {
                        iframeDocument = iframe.contentDocument;
                    }
                    else if (iframe.contentWindow) {
                        iframeDocument = iframe.contentWindow.document;
                    }

                    iframeDocument.open();
                    iframeDocument.writeln(iframeHtml);
                    iframeDocument.close();
                } else {
                    element.html('<span></span>');
                }
            }, true);
        }
    };
}

export default angular.module('directives.mjpeg', [])
    .directive('mjpeg', mjpeg)
    .name;
