import subprocess


domain = 'collective.todo'
i18ndude = '../../../../bin/i18ndude'


def rebuild():
    subprocess.call(
        [
            i18ndude,
            'rebuild-pot',
            '--pot',
            '{0}.pot'.format(domain),
            '--create',
            '{0}'.format(domain),
            '../',
        ]
    )


def update():
    rebuild()
    subprocess.call(
        [
            i18ndude,
            'sync',
            '--pot',
            '{0}.pot'.format(domain),
            '*/LC_MESSAGES/{0}.po'.format(domain),
        ]
    )


