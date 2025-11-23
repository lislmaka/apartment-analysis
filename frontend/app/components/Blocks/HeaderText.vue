<template>
    <div class="flex flex-col mt-10 mb-5">
        <primaryText class="text-3xl font-bold text-center text-gray-600">
            <slot name="primaryText"></slot>
        </primaryText>
        <secondaryText class="text-xl text-center text-gray-400">
            <slot name="secondaryText"></slot>
        </secondaryText>
    </div>
</template>