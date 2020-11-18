#/bin/bash
dvc commit -f
git commit -am "Experiment checkpoint"
git push origin $(git branch --show-current)
dvc push