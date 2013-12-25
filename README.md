WooCommerce SASS
===================

WooCommerce Styles with SASS.

In this project only convert the styles of front-end WooCommerce for SASS.

There was no modified styles of the original file in LESS.

## Requirements ##

* SASS
* WooCommerce 2.0.19 or later

## Installation ##

Add the files in the folder of your theme keeping this structure.

Run the following command to generate the css file:

```bash
compass compile
```

Paste in your functions.php:

```php
function cs_woocommerce_sass() {
    wp_enqueue_style( 'woocommerce-sass', get_template_directory_uri() . '/woocommerce-sass/css/woocommerce.css', array(), false, 'all' );
}

add_action( 'wp_enqueue_scripts', 'cs_woocommerce_sass' );
```

Now in the WooCommerce settings just deactivate the CSS.

## License ##

WooCommerce SASS is released under GPLv2.
