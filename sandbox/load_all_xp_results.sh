#/bin/bash
git fetch -a
git for-each-ref \
  --format="mkdir -p sandbox/%(refname:short) && git --work-tree=sandbox/%(refname:short) checkout  %(refname:short) -- out.npy.dvc square_err.metric;" \
  refs/remotes/ | xargs -I{} sh -c '{}'

dvc checkout -R sandbox