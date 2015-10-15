# -*- coding: utf-8 -*-


def update_links(sender, instance, **kwargs):
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    # Update all other link objects which have the same url with the new one
    sender.objects.filter(url=old_instance.url).exclude(pk=instance.pk).update(url=instance.url)