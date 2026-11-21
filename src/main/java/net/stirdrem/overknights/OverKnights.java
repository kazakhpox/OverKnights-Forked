package net.stirdrem.overknights;

import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import net.neoforged.neoforge.registries.DeferredHolder;
import net.neoforged.neoforge.registries.DeferredItem;
import net.neoforged.neoforge.registries.DeferredRegister;

/**
 * OverKnights: Knights &amp; Heraldry's arms and armour made the Overgeared way. The mod is mostly data: its recipes replace
 * Knights &amp; Heraldry's craftsman-anvil smithing with Overgeared forging (see {@code tools/gen_recipes.py}). It adds the few
 * parts Overgeared's way needs: chainmail mesh, leather strips and patches, woollen padding.
 */
@Mod(OverKnights.MOD_ID)
public final class OverKnights {
    public static final String MOD_ID = "overknights";

    public static final DeferredRegister.Items ITEMS = DeferredRegister.createItems(MOD_ID);
    public static final DeferredRegister<CreativeModeTab> TABS = DeferredRegister.create(Registries.CREATIVE_MODE_TAB, MOD_ID);

    public static final DeferredItem<Item> CHAINMAIL_MESH = ITEMS.registerSimpleItem("chainmail_mesh");
    public static final DeferredItem<Item> LEATHER_STRIP = ITEMS.registerSimpleItem("leather_strip");
    public static final DeferredItem<Item> LEATHER_PATCH = ITEMS.registerSimpleItem("leather_patch");
    public static final DeferredItem<Item> WOOLEN_PATCH = ITEMS.registerSimpleItem("woolen_patch");

    public static final DeferredHolder<CreativeModeTab, CreativeModeTab> TAB = TABS.register("overknights_tab", () -> CreativeModeTab.builder()
            .withTabsBefore(ResourceLocation.fromNamespaceAndPath("overgeared", "overgeared_tab"))
            .icon(() -> new ItemStack(CHAINMAIL_MESH.get()))
            .title(Component.translatable("creativetab.overknights_tab"))
            .displayItems((parameters, output) -> {
                output.accept(CHAINMAIL_MESH.get());
                output.accept(LEATHER_STRIP.get());
                output.accept(LEATHER_PATCH.get());
                output.accept(WOOLEN_PATCH.get());
            })
            .build());

    public OverKnights(IEventBus modBus) {
        ITEMS.register(modBus);
        TABS.register(modBus);
    }

    public static ResourceLocation id(String path) {
        return ResourceLocation.fromNamespaceAndPath(MOD_ID, path);
    }

    static boolean loaded(ResourceLocation item) {
        return BuiltInRegistries.ITEM.containsKey(item);
    }
}
