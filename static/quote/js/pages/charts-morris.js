$( document ).ready(function() {
    Morris.Area({
        element: 'morris1',
        data: [
            {period: '2017 Q1', iphone: 2666, ipad: 2100, itouch: 2647},
            {period: '2017 Q2', iphone: 2778, ipad: 2294, itouch: 2441},
            {period: '2017 Q3', iphone: 4912, ipad: 1969, itouch: 2501},
            {period: '2017 Q4', iphone: 3767, ipad: 3597, itouch: 5689},
            {period: '2018 Q1', iphone: 6810, ipad: 1914, itouch: 2293},
            {period: '2018 Q2', iphone: 5670, ipad: 4293, itouch: 1881},
            {period: '2018 Q3', iphone: 4820, ipad: 3795, itouch: 1588},
            {period: '2018 Q4', iphone: 15073, ipad: 5967, itouch: 5175},
            {period: '2019 Q1', iphone: 10687, ipad: 4460, itouch: 2028},
            {period: '2019 Q2', iphone: 8432, ipad: 5713, itouch: 1791}
        ],
        xkey: 'period',
        ykeys: ['iphone', 'ipad', 'itouch'],
        labels: ['Đơn đã đặt', 'Đơn đã thanh toán', 'Đơn bị hủy'],
        hideHover: 'auto',
        lineColors: ['#8adfd0', 'rgba(255, 206, 86, 1)','rgba(255, 99, 132, 0.5)'],
        resize: true,
    });
    
    /* Morris.Bar({
        element: 'morris2',
        data: [
            { year: '2006', a: 25, b: 15 },
            { year: '2007', a: 50, b: 40 },
            { year: '2008', a: 75, b: 65 },
            { year: '2009', a: 100, b: 90 },
            { year: '2010', a: 60, b: 50 },
            { year: '2011', a: 75, b: 65 },
            { year: '2012', a: 100, b: 90 } 
        ],
        xkey: 'year',
        ykeys: ['a', 'b'],
        labels: ['a', 'b'],
        barRatio: 0.4,
        xLabelAngle: 35,
        hideHover: 'auto',
        barColors: ['#6ad6c3','#30B19B'],
        resize: true
    });
    
    Morris.Line({
        element: 'morris3',
        data: [
            { year: '2006', a: 25, b: 15 },
            { year: '2007', a: 50, b: 40 },
            { year: '2008', a: 75, b: 65 },
            { year: '2009', a: 100, b: 90 },
            { year: '2010', a: 60, b: 50 },
            { year: '2011', a: 75, b: 65 },
            { year: '2012', a: 100, b: 90 } 
        ],
        xkey: 'year',
        ykeys: ['a', 'b'],
        labels: ['a', 'b'],
        resize: true,
        lineColors: ['#6ad6c3','#30B19B']
    }); */
    
    Morris.Donut({
        element: 'morris4',
        data: [
            {label: 'Đang vận chuyển', value: 30 },
            {label: 'Giao hàng thành công', value: 40 },
            {label: 'Đã thanh toán', value: 25 },
            {label: 'Hủy chuyến', value: 5 }
        ],
        resize: true,
        colors: ['#74e4d1', '#44cbb4', '#119d85','#30B19B'],
    });
});