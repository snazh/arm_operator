{
    'name': 'ARM Operator',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Simple operator model',
    'depends': ['web'],
    'data': [
        'views/task_views.xml',

    ],
    "assets": {
        "web.assets_backend": [
            "arm_operator/static/css/operator_task.css",
        ],

    },

    'installable': True,
    'auto_install': False,
    'application': True,

}
