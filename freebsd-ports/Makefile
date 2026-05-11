PORTNAME=		lce-qt-launcher
DISTVERSION=	26.5.11b0
CATEGORIES=		games python

MAINTAINER=		xgui4-dev@example.com
COMMENT=		Custom Free/Libre Minecraft Legacy Console Launcher
WWW=			https://github.com/xgui4/LCE-Qt-Launcher/

LICENSE=		GPLv3
LICENSE_FILE=	${WRKSRC}/license.md

# Dépendances de build
BUILD_DEPENDS=	bash:shells/bash \
		${PYTHON_PKGNAMEPREFIX}hatchling>0:devel/py-hatchling@${PY_FLAVOR}

# Dépendances d'exécution
RUN_DEPENDS=	bash:shells/bash \
				${PYTHON_PKGNAMEPREFIX}pyside6>0:devel/pyside6@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}hatch>0:devel/py-hatch@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}rich>0:devel/py-rich@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}vdf>0:devel/py-vdf@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}requests>0:devel/py-requests@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}platformdirs>0:devel/py-platformdirs@${PY_FLAVOR}

USES=			python qt:6 shebangfix
USE_GITHUB=		yes
GH_ACCOUNT=		xgui4
GH_PROJECT=		LCE-Qt-Launcher
GH_TAGNAME=		nightly

SHEBANG_FILES=	scripts/*.sh

USE_PYTHON=		autoplist pep517
USE_QT=			tools:build

.include <bsd.port.mk>
