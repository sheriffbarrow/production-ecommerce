from django.contrib import admin


from django.contrib.auth.admin import UserAdmin as UserAdminOrig
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from ecommerce.forms import UserCreationForm
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile, VendorSignUp

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import MyUser

# Register your models here.

class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm

	list_display = ('username','email','is_admin')
	list_filter = ('is_admin',)

	fieldsets = (
			(None, {'fields': ('username','email','password')}),
			('Permissions', {'fields': ('is_admin',)})
		)
	search_fields = ('username','email')
	ordering = ('username','email')

	filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)

admin.site.unregister(Group)



def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'






class UserAdmin(UserAdminOrig):
    readonly_fields = ('last_login', 'date_joined')
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'member')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_login', 'date_joined')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)
    add_form = UserCreationForm



class OrderAdmin(admin.ModelAdmin):
    list_display = ['email',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'email',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['email', 'street_address', 'apartment_address', 'zip']
class VendorSignUpAdmin(admin.ModelAdmin):
    list_display = ['email','location','phone','profession','experience','verified_id']
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['email','ordered','item','quantity']


admin.site.register(VendorSignUp, VendorSignUpAdmin)
admin.site.register(Item)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
