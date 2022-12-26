---
layout: "post"
title: "Multiple Galleries"
subtitle: "A post with multiple galleries arranged with ISOTOPE"
active: "journal"
image:
  feature: "pc007.jpg"
date: "2016-02-01"
header-img: "img/postcover/pc007.jpg"
comments: "true"
gallery1: 
  - image_path: /img/galleries/gallery01_big_island/DB9A9887_resized.webp
    caption: Pahoehoe Flow
    copyright: © takophotos
  - image_path: /img/galleries/gallery01_big_island/DB9A3786_resized.webp
    caption: Peepee Falls and Boiling Pots
    copyright: © takophotos
  - image_path: /img/galleries/gallery01_big_island/IMG-20211209-WA0018_resized.webp
    caption: Milkyway lava, Galactic Bulge.
    copyright: © takophotos
gallery2: 
  - image_path: /img/galleries/gallery10_honu/20210610_143845_046_resized.webp
    caption: Turtle or table?
    copyright: © takophotos
  - image_path: /img/galleries/gallery10_honu/GC6A6079_resized.webp
    caption: Baby guy
    copyright: © takophotos
  - image_path: /img/galleries/gallery10_honu/DB9A2772_resized.webp
    caption: Flapping along
    copyright: © takophotos
---


<html class="no-js" lang="en">
<head>
	<meta content="charset=utf-8">
</head>

    <body>

<section id="content" role="main">
		<div class="wrapper">
	<br><br>
			<h2>{{page.title}}</h2>




<p> Content of your post HERE </p>

<p> Add as many paragraphs amongst your galleries as you want. </p>


           <!-- Gallery __-->
			
{% include subgallery.html id="gallery1" %}

<!-- end of GALLERY __ -->

<p> Add as many galleries as you want, including as many photos as you want. Simply edit the <b>FRONT MATTER</b> of the post, adding the corresponding <b>path</b>, <b>caption</b> and <b>copyright</b> info for each one of your photos. </p>

           <!-- Gallery __-->
			
{% include subgallery.html id="gallery2" %}

<!-- end of GALLERY __ -->

		</div><!-- end of WRAPPER __ -->
	</section>


Photography by: <a href="https://www.instagram.com/cmutnik/">CMUTNIK</a>