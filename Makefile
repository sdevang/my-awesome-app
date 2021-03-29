.PHONY: patch-release minor-release major-release

patch-release: 
	bump2version patch
	git push --tags

minor-release:
	bump2version minor
	git push --tags

major-release:
	bump2version major
	git push --tags