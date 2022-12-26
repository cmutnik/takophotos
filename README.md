t a k o p h o t o s
====================

>---> [My Demo.](https://cmutnik.github.io/takophotos/ "DEMO")  <---<br>


----------
### Usage ###

** Before you begin: Change the URL and the BASEURL as well as the internal nav links in the `_config.yml` **

The **URL** should say `https://yourusername.github.io`

The **BASEURL** should say `/repositoryname`

**Internal nav** should say

  nav:

  - GALLERY: `"https://yourusername.github.io/repositoryname/gallery/"`
  - JOURNAL: `"https://yourusername.github.io/repositoryname/journal/"`
  - ABOUT: `"https://yourusername.github.io/repositoryname/about/`"

If there are problems with loading assets like CSS files and images, make sure that both **URL** and **BASEURL** are set correctly.

----

**Not for HTTPS served repos.**

If you want to use your **own domain** go to the root of your project's repository, create a CNAME file and add a line with your domain name, e.g. `www.yourdomain.com`.

Go to your domain name registrar and add a CNAME record pointing your domain to GitHub Pages:
- type: CNAME
- host: www.yourdomainname.com
- answer: yourusername.github.io/repositoryname
- TTL: 300

----
## Usage ##

### Quick Start ###

1. [Fork this repository](https://github.com/cmutnik/takophotos/fork) to get started. 
2. Go to `https://github.com/yourusername/takophotos/settings`
3. Rename the repository to your new project, e.g. *myphotoblog*
2. Create a new branch called `gh-pages` in your repository. 
3. Go to the branches directory at `https://github.com/yourusername/repositoryname/branches` and *change* **default branch** to **gh-pages**.
4. Delete **master** branch. 
3. GitHub will build your site automatically and publish it at `https://yourusername.github.io/repositoryname/`.  

