git clone https://github.com/username/repository.git
cd repository

# 2. Create and switch to a new branch
git checkout -b feature/new-functionality

# Or create with content:
echo "# Utilities package" > my_package/__init__.py

git add my_package/__init__.py
git commit -m "feat: add initial package"


# 5. Push branch to remote repository
git push origin feature/new-functionality